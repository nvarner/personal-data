import java.sql.ResultSet;

/**
 * Created by medude on 7/22/17.
 *
 * @author medude
 * @version 0.1
 */
public class Main {
    public static void main (String args[]) {
        try {
            DB personalInfo = new DB("jdbc:mysql://localhost/personal_data?useSSL=true",
                    new DBUser("sqluser", "sqluserpw"));
            personalInfo.update("INSERT INTO health values (0, '2017/7/22', 7879);");
            ResultSet resultSet = personalInfo.query("SELECT * FROM `health` ORDER BY `steps` DESC");

            resultSet.next();
            System.out.println(resultSet.getDate("date"));

            personalInfo.cleanup();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
