import java.net.InetAddress;
import java.rmi.*;
import java.io.*;
import java.util.Scanner;

public class MyClient{
	public static String str;
	public static void main(String args[]){

		try{
			String url = "rmi://"+ InetAddress.getLocalHost().getHostAddress()+":11223/japi";
			Method stub=(Method) Naming.lookup(url);  //replace 35.39.165.77 with your server's IP address
//			System.out.println(stub.action(3,4));

			do {
				Scanner scan = new Scanner(System.in);
				System.out.println("Enter String to Send to the server(Empty to Quit)");
				str = scan.nextLine();
				String stud = stub.getClient(str);

				if (str.equals("time")){
					System.out.println("[CLIENT] Callback: " + stub.action());
					System.out.println("[SERVER] RMI: " + stud);
				}
				else if(str.equals("")){
					break;
				}
				else {
					System.out.println("[CLIENT] Callback: " + str.toUpperCase());
					System.out.println("[SERVER] RMI: " + stud);
				}
			}while(true);

		}catch(Exception e){
			System.out.println(e);
		}//end catch

	}//end main
}//end class
