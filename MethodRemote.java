import java.rmi.*;
import java.rmi.server.*;
import java.util.Calendar;

public class MethodRemote extends UnicastRemoteObject implements Method{

	MethodRemote()throws RemoteException{
		super();
	}

	public String action(){
//		String timeStamp = new SimpleDateFormat("yyyy/MM/dd_HH:mm:ss").format(Calendar.getInstance().getTime());
		//		return String.valueOf(System.currentTimeMillis());
		return String.valueOf(Calendar.getInstance().getTime());
	}

	//callback implementation
	public String getClient(String Input){
		if(Input.equals("time")){
			return action();
		}else {
			return Input.toUpperCase();
		}
	}//end getClient
}//end Methodremote
