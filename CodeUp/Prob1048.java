/*
정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.
0 <= a <= 10, 0 <= b <= 10
 */

import java.util.Scanner;

public class Prob1048 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();

        int result = (int)Math.pow(2, b);
        System.out.println(a * result);
    }
}
