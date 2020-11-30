/*
실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
 */

import java.util.*;

public class Prob1023 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        String[] arr = input.split("\\.");
        System.out.println(Integer.parseInt(arr[0]));
        System.out.println(Integer.parseInt(arr[1]));
    }
}
