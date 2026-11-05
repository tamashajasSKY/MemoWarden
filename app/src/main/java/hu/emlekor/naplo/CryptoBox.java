package hu.emlekor.naplo;
import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
/** Portable authenticated encryption, shared by backup and native local vault. */
public final class CryptoBox {
    private static final SecureRandom RANDOM=new SecureRandom();
    private static final int ITERATIONS=210000;
    private static byte[] random(int length){byte[] b=new byte[length];RANDOM.nextBytes(b);return b;}
    private static String b64(byte[] b){return Base64.getEncoder().encodeToString(b);}
    private static byte[] unb64(String s){return Base64.getDecoder().decode(s);}
    private static SecretKey derive(char[] password,byte[] salt)throws Exception{PBEKeySpec spec=new PBEKeySpec(password,salt,ITERATIONS,256);try{return new SecretKeySpec(SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256").generateSecret(spec).getEncoded(),"AES");}finally{spec.clearPassword();}}
    public static String seal(SecretKey key,String raw,String context)throws Exception{Cipher c=Cipher.getInstance("AES/GCM/NoPadding");c.init(Cipher.ENCRYPT_MODE,key);c.updateAAD(context.getBytes(StandardCharsets.UTF_8));return b64(c.getIV())+"\n"+b64(c.doFinal(raw.getBytes(StandardCharsets.UTF_8)));}
    public static String open(SecretKey key,String encrypted,String context)throws Exception{String[] p=encrypted.split("\n",-1);if(p.length!=2)throw new Exception("format");byte[] iv=unb64(p[0]);if(iv.length!=12)throw new Exception("iv");Cipher c=Cipher.getInstance("AES/GCM/NoPadding");c.init(Cipher.DECRYPT_MODE,key,new GCMParameterSpec(128,iv));c.updateAAD(context.getBytes(StandardCharsets.UTF_8));return new String(c.doFinal(unb64(p[1])),StandardCharsets.UTF_8);}
    public static String exportBackup(String raw,char[] password)throws Exception{byte[] salt=random(16);return "EMLEKOR1\n"+ITERATIONS+"\n"+b64(salt)+"\n"+seal(derive(password,salt),raw,"emlekor.backup.v1");}
    public static String importBackup(String raw,char[] password)throws Exception{if(raw.length()>12000000)throw new Exception("size");String[] p=raw.trim().split("\n",-1);if(p.length!=5||!p[0].equals("EMLEKOR1")||!p[1].equals(Integer.toString(ITERATIONS)))throw new Exception("format");byte[] salt=unb64(p[2]);if(salt.length!=16)throw new Exception("salt");return open(derive(password,salt),p[3]+"\n"+p[4],"emlekor.backup.v1");}
}
