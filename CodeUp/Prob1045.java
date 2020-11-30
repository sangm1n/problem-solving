/*
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단 0 <= a, b <= 2147483647, b는 0이 아니다.
 */

import java.util.Scanner;

public class Prob1045 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        float a = scan.nextInt();
        float b = scan.nextInt();

        float sum = a + b;
        float sub = a - b;
        float mul = a * b;
        float mok = a / b;
        float mod = a % b;
        float div = a / b;

        System.out.printf("%d%n%d%n%d%n%d%n%d%n%.2f%n",
                (long)sum, (long)sub, (long)mul, (long)mok, (long)mod, div);
    }
}
