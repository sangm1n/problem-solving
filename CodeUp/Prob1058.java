/*
두 개의 참(1) 또는 거짓(0)이 입력될 때,
모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
 */

import java.util.Scanner;

public class Prob1058 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();

        if (a == 0 && b == 0) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
