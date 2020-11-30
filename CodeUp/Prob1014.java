/*
2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
 */

import java.util.*;

public class Prob1014 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        char a, b;
        a = input.charAt(0);
        b = input.charAt(2);
        System.out.println(b + " " + a);
    }
}
