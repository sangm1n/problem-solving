/*
두 정수(a, b)를 입력받아
a와 b가 같으면 1을, 같지 않으면 0을 출력하는 프로그램을 작성해보자.
 */

import java.util.Scanner;

public class Prob1050 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();

        int result = (a == b) ? 1 : 0;
        System.out.println(result);
    }
}
