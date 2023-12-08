
import com.alibaba.fastjson.JSONObject;
import java.io.*;
import java.net.Socket;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class Transporter {
    private Socket socket;
    private BufferedReader reader;
    private BufferedWriter writer;

    public Transporter(Socket socket) throws IOException {
        this.socket = socket;
        this.reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        this.writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream(),"UTF-8"));
//        this.writer = new BufferedWriter(socket.getOutputStream(),"UTF-8");
    }

    public void send(DataMessage dataMessage) throws Exception {
//        JSONObject js= (JSONObject) JSONObject.toJSON(dataMessage);

        String msg=JSONObject.toJSONString(dataMessage);
        System.out.println(msg);
        writer.write(msg+"[O]");
        writer.flush();
    }

    public String receive() throws Exception {
        // line是一个16进制数 0073656c656374202a2066726f6d207361696c6f72
        String line = reader.readLine();
        System.out.println(line);
        if(line == null) {
            close();
        }
//        return hexDecode(line);
        return line;
    }

    public void close() throws IOException {
        writer.close();
        reader.close();
        socket.close();
    }

//    private String hexEncode(byte[] buf) {
//        return Hex.encodeHexString(buf, true)+"\n";
//    }
//
//    private byte[] hexDecode(String buf) throws DecoderException {
//        return Hex.decodeHex(buf);
//    }
}

