package hu.emlekor.naplo;
import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.webkit.*;
import java.io.ByteArrayInputStream;
import org.json.JSONObject;
public final class MainActivity extends Activity {
    private WebView web;private MemoryBridge bridge;
    @Override public void onCreate(Bundle b){super.onCreate(b);getWindow().setStatusBarColor(0xfff6f4ee);getWindow().setNavigationBarColor(0xfffaf9f3);getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR|View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR);web=new WebView(this);web.setBackgroundColor(0xfff6f4ee);WebSettings s=web.getSettings();s.setJavaScriptEnabled(true);s.setDomStorageEnabled(false);s.setAllowFileAccess(true);s.setAllowContentAccess(false);s.setAllowFileAccessFromFileURLs(false);s.setAllowUniversalAccessFromFileURLs(false);s.setSupportZoom(false);s.setCacheMode(WebSettings.LOAD_NO_CACHE);web.setWebViewClient(new WebViewClient(){@Override public boolean shouldOverrideUrlLoading(WebView v,WebResourceRequest r){return true;}@Override public WebResourceResponse shouldInterceptRequest(WebView v,WebResourceRequest r){if(r.getUrl().toString().startsWith("file:///android_asset/"))return null;return new WebResourceResponse("text/plain","UTF-8",new ByteArrayInputStream(new byte[0]));}});bridge=new MemoryBridge(this,(kind,data)->runOnUiThread(()->{if(web!=null)web.evaluateJavascript("window.App&&window.App.receive("+JSONObject.quote(kind)+","+JSONObject.quote(data)+");",null);}));web.addJavascriptInterface(bridge,"MemoryNative");android.widget.FrameLayout root=new android.widget.FrameLayout(this);root.addView(web,new android.widget.FrameLayout.LayoutParams(-1,-1));if(android.os.Build.VERSION.SDK_INT>=30){getWindow().setDecorFitsSystemWindows(false);root.setOnApplyWindowInsetsListener((view,insets)->{android.graphics.Insets edges=insets.getInsets(android.view.WindowInsets.Type.systemBars()|android.view.WindowInsets.Type.ime());view.setPadding(edges.left,edges.top,edges.right,edges.bottom);return insets;});}setContentView(root);web.loadUrl("file:///android_asset/index.html");}
    @Override protected void onPause(){if(web!=null){web.evaluateJavascript("window.App&&window.App.flush();",null);web.onPause();}super.onPause();}
    @Override protected void onResume(){super.onResume();if(web!=null)web.onResume();}
    @Override public void onBackPressed(){if(web!=null)web.evaluateJavascript("window.App&&window.App.back();",null);}
    @Override protected void onActivityResult(int request,int result,android.content.Intent data){super.onActivityResult(request,result,data);if(bridge!=null)bridge.result(request,result,data);}
    @Override protected void onDestroy(){if(bridge!=null)bridge.destroy();if(web!=null){web.removeJavascriptInterface("MemoryNative");web.destroy();web=null;}super.onDestroy();}
}
