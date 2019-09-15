The master branch is for the Django app and the Java Branch is for... the java program.  

This is basically the Java code for random number generator-
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;
and then within the servlet we need to place 
        Random rand  = new Random();
        int num = rand.nextInt(1000000);
        num += 1;

For Java on Compute Engine:

This video will get you started with Tomcat on ComputeEngine- https://youtu.be/CXHnfscyIsU once you have the generic page working you can modify their hello world example and just drop those lines in the code like this-
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ResourceBundle;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
/**
 * The simplest possible servlet.
 *
 * @author James Duncan Davidson
 */
public class HelloWorldExample extends HttpServlet {
    private static final long serialVersionUID = 1L;
    @Override
    public void doGet(HttpServletRequest request,
                      HttpServletResponse response)
        throws IOException, ServletException
    {
        ResourceBundle rb =
            ResourceBundle.getBundle("LocalStrings",request.getLocale());
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<!DOCTYPE html><html>");
        out.println("<head>");
        out.println("<meta charset=\"UTF-8\" />");
        String title = rb.getString("helloworld.title");
        out.println("</head>");
        out.println("<body bgcolor=\"white\">");

        //INSERT CODE HERE
        PrintWriter printWriter  = response.getWriter();
        Random rand  = new Random();
        int num = rand.nextInt(1000000);
        num += 1;
        out.println( num );
        //END OF OUR CODE
        out.println("</body>");
        out.println("</html>");
    }
}






Java on App-Engine-
https://github.com/SlidingSteven/JavaAppEngine  
There is a tutorial on Java apps on app engine which I followed to get up and running.  Next I edited  
~/appengine-try-java/src/main/java/myapp/DemoServlet.java file to show- 
/*

 * Copyright 2016 Google Inc. All Rights Reserved.

 *
 * Licensed under the
 Apache License, Version 2.0 (the "License");

 * you may not use this file except in compliance with the License.

 * You may obtain a copy of the License at

 *
 *

http://www.apache.org/licenses/LICENSE-2.0

 *
 * Unless required by
 applicable law or agreed to in writing, software

 * distributed under the License is distributed on an "AS IS" BASIS,

 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

 * See the License for the specific language governing permissions and

 * limitations under the License.

 */
package
 myapp;
import java.io.PrintWriter;
import
 java.util.Random;
import
 java.io.IOException;
import
 javax.servlet.http.HttpServlet;
import
 javax.servlet.http.HttpServletRequest;
import
 javax.servlet.http.HttpServletResponse;
public
class DemoServlet 
extends HttpServlet {
 @Override

public void
doGet(HttpServletRequest req, HttpServletResponse resp)

throws IOException {
 resp.setContentType("text/plain");
//
 PrintWriter printWriter = response.getWriter();
 Random rand
 = new Random();

int num = rand.nextInt(1000000);

 num += 1;
// int code = 500;

 resp.getWriter().println("{ \"name\": \""+num+"\" }");

 }
}

which passes our random int to the index page.

How to run:

For both App Engine and the Virtual Machine, the user should simply click the URLs provided in this document. Refreshing the page will display another random number from 1 to 1,000,000.

This link will take you to the Java program that runs the random number generator: http://final-java-attempt.appspot.com/

The Java implementation for the VM can be reached through this link: http://34.82.94.25/examples/servlets/servlet/HelloWorldExample

The Python code on app engine runs when the user clicks this link: https://helloworldpython-252906.appspot.com/

The Python implementation can be accessed from this link.

In all of these cases, it is important that the app is launched and enabled for the user to be able to see the number.

