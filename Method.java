import java.rmi.*;

public interface Method extends Remote{

	public String action()throws RemoteException;

	//callback implementation
	public String getClient(String Input) throws  RemoteException;
}
