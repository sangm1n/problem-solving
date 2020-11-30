/*
단어를 1개 입력받는다.

입력받은 단어(영어)의 각 문자를

한줄에 한 문자씩 분리해 출력한다.
 */

import java.util.*;

public class Prob1024 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        String[] arr = input.split("");

        for (int i = 0; i < arr.length; i++) {
            System.out.println("'" + arr[i] + "'");
        }
    }
}
