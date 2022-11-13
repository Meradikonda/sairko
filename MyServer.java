import java.net.InetAddress;
import java.net.MalformedURLException;
import java.net.UnknownHostException;
import java.rmi.*;
import java.rmi.registry.*;
import java.rmi.RemoteException;
import java.rmi.server.*;

public class MyServer{

	public static void main(String args[]){

		try {

			MethodRemote stub = new MethodRemote();
			MyClient obj = new MyClient();


			Registry registry = LocateRegistry.createRegistry(11223);

			String url = "rmi://"+ InetAddress.getLocalHost().getHostAddress()+":11223/japi";
			Naming.rebind(url, stub);

			System.out.println("[SERVER] " + url + " Started...");
//			stub.getClient(obj.str);
		} catch (RemoteException | UnknownHostException | MalformedURLException e) {
			System.out.println("server error" + e);
		}

	}
}

