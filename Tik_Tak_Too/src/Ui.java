import com.raylib.Raylib;

public class Ui {
    public static void main(String[] args) {
        Raylib rl = new Raylib(800, 450, "Hello raylib (Java)");

        while (!rl.windowShouldClose()) {
            rl.beginDrawing();
            rl.clearBackground(Raylib.RAYWHITE);
            rl.drawText("Hello raylib!", 250, 200, 20, Raylib.BLACK);
            rl.endDrawing();
        }

        rl.closeWindow();
    }
}
