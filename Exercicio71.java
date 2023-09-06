import java.util.Scanner;

public class Exercicio71 {
    public static void main (String[] args){
        Scanner sr = new Scanner(System.in);
        System.out.print("digite o dinheiro que quer sacar: ");
        int dinheiro_sacar = sr.nextInt();
        int [] cedulas = {50,20,10,1};
        sr.close();

        for(int cedula_disponivel =0; cedula_disponivel < cedulas.length;cedula_disponivel++){
            if(dinheiro_sacar >=cedulas[cedula_disponivel]){
            int nota = (int) dinheiro_sacar/cedulas[cedula_disponivel];
            System.out.printf("Imprimiu %d de %d  %n",nota, cedulas[cedula_disponivel]);
            dinheiro_sacar -= nota*cedulas[cedula_disponivel];
            }
        }


    }
}
