/*
1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때
반대로 출력하는 프로그램을 작성해보자.
 */

import java.util.Scanner;

public class Prob1053 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int bool = scan.nextInt();
        if (bool == 1) {
            System.out.println(0);
        } else if (bool == 0) {
            System.out.println(1);
        }
    }
}
