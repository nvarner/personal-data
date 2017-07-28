import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Arrays;

/**
 * Created by medude on 7/23/17.
 *
 * @author medude
 * @version 0.1
 */
public class DBUser {
    private String username;
    private String password;
    byte[] codeWord = null;

    public DBUser (String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String getCodeWord () {
        if (codeWord == null) {
            SecureRandom random = new SecureRandom();
            String unhashedCodeword = new BigInteger(130, random).toString(32);

            try {
                MessageDigest md = MessageDigest.getInstance("SHA-256");
                md.update(unhashedCodeword.getBytes("UTF-8"));

                this.codeWord = md.digest();
            } catch (Exception e) {
                System.out.println("There was a problem with securing your codeword.");
                System.exit(-1);
            }

            return unhashedCodeword;
        } else {
            throw new SecurityException("Codeword already generated! Store it the first time, and/or stop hacking. " +
                    "It's not very nice.");
        }
    }

    public String getUsername (String codeWord) throws NoSuchAlgorithmException, UnsupportedEncodingException,
            SecurityException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(codeWord.getBytes("UTF-8"));
        if (this.codeWord == null) {
            throw new SecurityException("Codeword not generated! Generate the codeword and store it with getCodeWord " +
                    "before using it.");
        } else if (Arrays.equals(this.codeWord, md.digest())) {
            return  username;
        } else {
            throw new SecurityException("Bad codeword! Store it from getCodeword to use it.");
        }
    }

    public String getPassword (String codeWord) throws NoSuchAlgorithmException, UnsupportedEncodingException,
            SecurityException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(codeWord.getBytes("UTF-8"));
        if (this.codeWord == null) {
            throw new SecurityException("Codeword not generated! Generate the codeword and store it with getCodeWord " +
                    "before using it.");
        } else if (Arrays.equals(this.codeWord, md.digest())) {
            return  password;
        } else {
            throw new SecurityException("Bad codeword! Store it from getCodeword to use it.");
        }
    }
}
