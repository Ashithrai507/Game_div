#include "raylib.h"
#include "player.h"

int main() {
    InitWindow(1200, 700, "Goal Example");
    SetTargetFPS(60);

    Player player;
    player.Init("assets/player.png", {300, 300});
    Texture2D goalTex = LoadTexture("assets/goal.png");

    Texture2D bg = LoadTexture("assets/bg.png");

    Rectangle goal = { 900, 500, 100, 150 };
    bool levelComplete = false;

    while (!WindowShouldClose()) {
        float dt = GetFrameTime();

        // ---------------- UPDATE ----------------
        if (!levelComplete) {
            player.Update(dt);
        }

        // Build player hitbox
        float spriteW = player.frameWidth * player.scale;
        float spriteH = player.frameHeight * player.scale;

        Rectangle playerBox = {
            player.pos.x,
            player.pos.y - spriteH,
            spriteW,
            spriteH
        };

        // -------- FLOOR COLLISION ----------
        bool landed = false;

        if (playerBox.y + playerBox.height > GetScreenHeight()) {
            player.pos.y = GetScreenHeight();
            landed = true;
        }

        // Notify landing
        if (landed) {
            player.Land();
        } else {
            if (player.isGrounded) {
                player.LeaveGround();
            }
        }

        // -------- GOAL COLLISION ----------
        if (CheckCollisionRecs(playerBox, goal)) {
            levelComplete = true;
        }

        // ---------------- DRAW ----------------
        BeginDrawing();
        ClearBackground(RAYWHITE);

        DrawTexture(bg, 0, 0, WHITE);

        // draw goal
        DrawTexturePro(
            goalTex,
            {0, 0, (float)goalTex.width, (float)goalTex.height}, // source
            {goal.x, goal.y, goal.width, goal.height},            // destination (scaled)
            {0, 0},                                               // origin
            0.0f,
            WHITE
        );


        if (levelComplete) {
            DrawText("LEVEL COMPLETE!", 420, 300, 40, GREEN);
        }

        player.Draw();

        EndDrawing();
    }

    CloseWindow();
    return 0;
}
