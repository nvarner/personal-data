import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;
import java.sql.*;

/**
 * Created by medude on 7/23/17.
 *
 * @author medude
 * @version 0.1
 */
public class DB {
    private final String URL;
    private final String DRIVER = "com.mysql.jdbc.Driver";
    private DBUser user;
    private String codeword;

    private Connection connection;
    private Statement statement;

    public DB (String url, DBUser user) throws ClassNotFoundException, NoSuchAlgorithmException,
    UnsupportedEncodingException, SQLException{
        this.URL = url;
        this.user = user;
        this.codeword = this.user.getCodeWord();

        Class.forName(DRIVER);

        this.connection = DriverManager.getConnection(URL, user.getUsername(codeword), user.getPassword(codeword));
        this.statement = connection.createStatement();
    }

    public int update (String statementString) throws SQLException {
        return this.statement.executeUpdate(statementString);
    }

    public ResultSet query (String statementString) throws SQLException {
        return this.statement.executeQuery(statementString);
    }

    public void cleanup () throws SQLException {
        statement.close();
        connection.close();
    }
}
