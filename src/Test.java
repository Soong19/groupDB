public class Test {
    public static void main(String[] args) {
        Operating operating = new Operating();

        try {
            operating.login();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}