import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;
import javax.servlet.annotation.WebServlet;
@WebServlet("/Log")
public class Log extends HttpServlet {
    public void doPost(HttpServletRequest req, HttpServletResponse res)throws ServletException, IOException
	{
        String query;
        String dbemail, dbPassword;
		String email,password;

	    email = req.getParameter("email");
		password = req.getParameter("password");

      PrintWriter pn = res.getWriter();
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/hospital?useSSl=false", "root", "santosh71$");
            Statement stmt =  con.createStatement();
            query = "SELECT email, password FROM hospital";
            stmt.executeQuery(query);
            ResultSet rs = stmt.getResultSet();

            while(rs.next()){
                dbemail = rs.getString("email");
                dbPassword = rs.getString("password");

                if(dbemail.equals(email) && dbPassword.equals(password)){

		       res.sendRedirect("home.html");
                }
                else
                {
                res.sendRedirect("login.jsp");
                }
            }
		}
        catch(Exception se)
        {
            se.printStackTrace();
        }


	}
}