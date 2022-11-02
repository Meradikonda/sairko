import java.rmi.*;
import java.rmi.server.*;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class MethodRemote extends UnicastRemoteObject implements Method{

	MethodRemote()throws RemoteException{
		super();
	}

	public String action(){
//		String timeStamp = new SimpleDateFormat("yyyy/MM/dd_HH:mm:ss").format(Calendar.getInstance().getTime());
		String timeStamp = String.valueOf(Calendar.getInstance().getTime());
//		return String.valueOf(System.currentTimeMillis());
		return timeStamp;
	}
}
