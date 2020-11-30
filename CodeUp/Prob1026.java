/*
입력되는 시:분:초 에서 분만 출력해보자.
 */

import java.util.*;

public class Prob1026 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        String[] arr = input.split(":");

        System.out.println(arr[1]);
    }
}
