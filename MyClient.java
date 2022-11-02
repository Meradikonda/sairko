import java.net.InetAddress;
import java.rmi.*;
import java.io.*;
import java.util.Scanner;

public class MyClient{

	public static void main(String args[]){

		try{
			String url = "rmi://"+ InetAddress.getLocalHost().getHostAddress()+":11223/BankAccount";
			Method stub=(Method) Naming.lookup(url);  //replace 35.39.165.77 with your server's IP address
//			System.out.println(stub.action(3,4));

			do {
				Scanner scan = new Scanner(System.in);
				System.out.println("=>");
				String str = scan.nextLine();

				if (str.equals("time")){
					System.out.println(stub.action());
				}
				else if(str.equals("")){
					break;
				}
				else {
					System.out.println(str.toUpperCase());
				}
			}while(true);

		}catch(Exception e){System.out.println(e);}


	}
}
