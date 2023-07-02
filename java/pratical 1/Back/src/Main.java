public class Main {
    public static void main(String[] args) {

        Account object=new Account();
        object.deposit(1000);
        System.out.println(object.getBalance());
        object.deposit(2000);
        System.out.println(object.getBalance());
        object.withdraw(1500);
        System.out.println(object.getBalance());
    }
}

class Account{
    int account;
    float balance;
    Account(){
        account=0;
        balance=0;
    }
    float getBalance(){
        return balance;
    }
    int getAccount(){
        return account;
    }
    void deposit(float k){
        balance+=k;
    }
    void withdraw(int k){
        balance-=k;
    }

}