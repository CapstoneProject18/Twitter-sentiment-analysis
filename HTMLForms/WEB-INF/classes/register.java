
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;
import javax.servlet.annotation.WebServlet;
@WebServlet("/register")
public class register extends HttpServlet {

    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        String username = request.getParameter("username");

        String password = request.getParameter("password");

        String email = request.getParameter("email");

        String mobilenumber = request.getParameter ("mobilenumber");


        try{

        //loading drivers for mysql
        Class.forName("com.mysql.jdbc.Driver");

	//creating connection with the database
          Connection con=DriverManager.getConnection ("jdbc:mysql://localhost/hospital?useSSl=false","root","santosh71$");

        PreparedStatement ps=con.prepareStatement("insert into hospital values(?,?,?,?)");

        ps.setString(1,username);

        ps.setString(2,password);
        ps.setString(3,email);
        ps.setString(4,mobilenumber);
        int i=ps.executeUpdate();
        if(i>0)
          {
            out.println("You are sucessfully registered");
             RequestDispatcher rs = request.getRequestDispatcher("login.jsp");
            rs.forward(request, response);
          }

        }
        catch(Exception se)
        {
            se.printStackTrace();
        }

      }
}