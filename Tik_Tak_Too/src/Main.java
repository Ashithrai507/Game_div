import java.util.Scanner;
class Main{
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int board[] = new int[9];
    System.out.println("Welcome to Tic Tac Toe Game");
    System.out.println("Player 1 -> X & Player 2 -> o");   
    System.out.println("Positions\n p1 | p2 | p3 \n --   --   --  \n p4 | p5 | p6 \n --   --   --  \n p7 | p8 | p9");
    for(int i=0; i<9; i++){
        System.out.println("Player " + (i%2 + 1) + " turn");
        int pos = sc.nextInt();
        if(board[pos-1] == 0){
            board[pos-1] = (i%2 + 1);
        }else{
            System.out.println("Position already occupied. Try again.");
            i--;
            continue;
        }
        if(checkWin(board, i%2 + 1)){
            System.out.println("Player " + (i%2 + 1) + " wins!");
            return;
        }
    }
    System.out.println("It's a draw!");
}

    private static boolean checkWin(int[] board, int i) {
        int[][] winPositions = {
            {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, 
            {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
            {0, 4, 8}, {2, 4, 6}            
        };
        for (int[] pos : winPositions) {
            if (board[pos[0]] == i && board[pos[1]] == i && board[pos[2]] == i) {
                return true;
            }
        }
        return false;
    }
}
