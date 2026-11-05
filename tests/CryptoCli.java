import hu.emlekor.naplo.CryptoBox;
import java.io.*;
import java.nio.charset.StandardCharsets;
public class CryptoCli {
 public static void main(String[] args)throws Exception {ByteArrayOutputStream out=new ByteArrayOutputStream();byte[] b=new byte[8192];int n;while((n=System.in.read(b))!=-1)out.write(b,0,n);String raw=new String(out.toByteArray(),StandardCharsets.UTF_8);System.out.print(args[0].equals("encrypt")?CryptoBox.exportBackup(raw,args[1].toCharArray()):CryptoBox.importBackup(raw,args[1].toCharArray()));}
}
