/*
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
 */

import java.util.*;

public class Prob1032 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();
        System.out.printf("%x", num);
    }
}
