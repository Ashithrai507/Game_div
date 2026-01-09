#include "raylib.h"
#include "player.h"

// ------------------------
// GAME STATES / LEVELS
// ------------------------
enum GameState {
    LEVEL1,
    LEVEL2
};

GameState state = LEVEL1;
int currentLevel = 1;

// Global level objects
Texture2D tableTex = {0};
Texture2D obj = {0};
Rectangle tableRect = {0};

// ------------------------
// LOAD LEVEL DATA HERE
// ------------------------
void LoadLevel(int level, Texture2D &bg, Rectangle &goal, Player &player) {

    // Unload previous background if needed
    if (bg.id > 0) {
        UnloadTexture(bg);
    }
    // unload table texture to avoid memory leaks
    if (tableTex.id > 0) UnloadTexture(tableTex);
    if (obj.id > 0) UnloadTexture(obj);


    if (level == 1) {
        bg = LoadTexture("assets/bg.jpeg");
        goal =  { 1050, 380, 120, 240 };
        player.pos = { 200.0f, 350.0f };
        //tableTex = LoadTexture("assets/obj.png");
        //tableRect = { 500, 500, 120, 120 }; 
    }

    if (level == 2) {
        obj = LoadTexture("assets/obj.png");
        bg = LoadTexture("assets/bg2.png");
        // slightly larger goal for level 2 as well
        goal = { 1050, 480, 96, 168 };
        player.pos = { 150.0f, 350.0f };
    }

    // you can add platforms, spikes, traps here later
}

int main() {
    InitWindow(1200, 700, "Multi-Level Platformer");
    SetTargetFPS(60);

    // Player
    Player player;
    player.Init("assets/player.png", {100, 300});

    // Level objects
    Texture2D bg = {0};
    Rectangle goal;

    // Initial Level Load
    LoadLevel(currentLevel, bg, goal, player);

    // Goal texture (door)
    Texture2D goalTex = LoadTexture("assets/goal.jpeg");

    while (!WindowShouldClose()) {

        float dt = GetFrameTime();

        // =======================
        // UPDATE PLAYER (if no transition)
        // =======================
        player.Update(dt);

        // Build hitbox
        float spriteW = player.frameWidth * player.scale;
        float spriteH = player.frameHeight * player.scale;

        Rectangle playerBox = {
            player.pos.x,
            player.pos.y - spriteH,
            spriteW,
            spriteH
        };

        // ----------------------
        // BASIC FLOOR COLLISION
        // ----------------------
        bool landed = false;

        if (playerBox.y + playerBox.height > GetScreenHeight()) {
            player.pos.y = GetScreenHeight();
            landed = true;
        }

        if (landed) player.Land();
        else if (player.isGrounded) player.LeaveGround();

        // ----------------------
        // GOAL COLLISION → NEXT LEVEL
        // ----------------------
        if (CheckCollisionRecs(playerBox, goal)) {
            currentLevel++;

            if (currentLevel > 2) {
                currentLevel = 1;   // loop back to level 1
            }

            LoadLevel(currentLevel, bg, goal, player);
            continue;   // skip this frame to avoid double drawing
        }

        // =======================
        // DRAW
        // =======================
        BeginDrawing();
        ClearBackground(RAYWHITE);

        // Background - draw stretched to the current window size so it matches the screen
        DrawTexturePro(
            bg,
            { 0, 0, (float)bg.width, (float)bg.height },
            { 0, 0, (float)GetScreenWidth(), (float)GetScreenHeight() },
            { 0, 0 },
            0.0f,
            WHITE
        );

        /*if (currentLevel == 1) {
                DrawTexturePro(
                    tableTex,
                    {0, 0, (float)tableTex.width, (float)tableTex.height},
                    {tableRect.x, tableRect.y, tableRect.width, tableRect.height},
                    {0, 0},
                    0.0f,
                    WHITE
                );
            }*/

        // Draw goal door
        DrawTexturePro(
            goalTex,
            {0, 0, (float)goalTex.width, (float)goalTex.height},
            {goal.x, goal.y, goal.width, goal.height},
            {0, 0},
            0.0f,
            WHITE
        );

        player.Draw();

        EndDrawing();
    }

    // Clean up
    UnloadTexture(bg);
    CloseWindow();
    return 0;
}
