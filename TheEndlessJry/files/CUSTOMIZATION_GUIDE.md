# Customization & Modding Guide

## How to Customize Your Game

The game is built with easy-to-modify code. Here's how to customize different aspects:

---

## Visual Customization

### Change Plane Color

Find this section (around line 450):
```javascript
const fuselage = new THREE.Mesh(
    new THREE.ConeGeometry(8, 50, 8),
    new THREE.MeshPhongMaterial({ color: 0xff0000 })  // <-- Red
);
```

Change `0xff0000` to any hex color:
- `0x00ff00` = Green
- `0x0000ff` = Blue
- `0xffff00` = Yellow
- `0xff00ff` = Magenta
- `0x00ffff` = Cyan

### Change Sky Color

Find this section (around line 380):
```javascript
const skyGeometry = new THREE.SphereGeometry(30000, 32, 32);
const skyMaterial = new THREE.MeshBasicMaterial({
    color: 0x87ceeb,  // <-- Sky blue
    side: THREE.BackSide
});
```

Try these colors:
- `0x87ceeb` = Light blue (default)
- `0x1a1a2e` = Dark night sky
- `0xff6b35` = Orange sunset
- `0x2a9d8f` = Teal ocean

### Change Terrain Colors

Find the terrain generation section (around line 280):
```javascript
colors.push(
    0.2 + normalizedHeight * 0.3,  // Red component
    0.4 + normalizedHeight * 0.2,  // Green component
    0.1                             // Blue component
);
```

Experiment with different values (0.0 to 1.0):
- Increase red for more desert terrain
- Increase green for grasslands
- Increase blue for more water-like appearance

### Change HUD Color

Find this section (around line 70):
```css
#hud {
    color: #00ff41;  /* Bright green */
    text-shadow: 0 0 10px #00ff41;
}

.hud-panel {
    border: 2px solid #00ff41;
    box-shadow: 0 0 20px rgba(0, 255, 65, 0.3);
}
```

Try these color schemes:

**Cyan Futuristic:**
```css
color: #00ffff;
border: 2px solid #00ffff;
text-shadow: 0 0 10px #00ffff;
box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
```

**Orange Warm:**
```css
color: #ff6600;
border: 2px solid #ff6600;
text-shadow: 0 0 10px #ff6600;
box-shadow: 0 0 20px rgba(255, 102, 0, 0.3);
```

**Purple Neon:**
```css
color: #ff00ff;
border: 2px solid #ff00ff;
text-shadow: 0 0 10px #ff00ff;
box-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
```

---

## Gameplay Customization

### Adjust Difficulty

**Easy Mode** - More fuel, less gravity:
```javascript
gameState.plane.fuel = 150;  // More fuel
gameState.plane.speed = 120; // Higher default speed
// In physics section, change: gameState.plane.velocity.y -= 0.2; // Less gravity
```

**Hard Mode** - Less fuel, faster consumption:
```javascript
gameState.plane.fuel = 50;   // Less fuel
// In fuel section, change: gameState.plane.fuel -= 0.05; // Faster drain
```

### Change Flight Responsiveness

Find this section (around line 570):
```javascript
gameState.plane.pitch += (gameState.mouse.normY * maxPitch - gameState.plane.pitch) * 0.1;
gameState.plane.roll += (gameState.mouse.normX * maxRoll - gameState.plane.roll) * 0.1;
```

The `0.1` controls sensitivity:
- `0.05` = Slower, smoother controls
- `0.1` = Default (moderate)
- `0.2` = Faster, snappier response

### Increase Maximum Altitude

Find this section (around line 610):
```javascript
if (gameState.plane.position.y > 3000) {
    gameState.plane.position.y = 3000;
}
```

Change `3000` to higher value:
- `5000` = Much higher ceiling
- `10000` = Extreme altitude

### Change Speed Range

Find the scroll handler (around line 520):
```javascript
gameState.plane.speed = Math.max(20, Math.min(200, gameState.plane.speed + (e.deltaY > 0 ? -2 : 2)));
```

Adjust these values:
- `20` = Minimum speed
- `200` = Maximum speed
- `2` = Speed increment per scroll

Example (faster throttle):
```javascript
gameState.plane.speed = Math.max(50, Math.min(300, gameState.plane.speed + (e.deltaY > 0 ? -5 : 5)));
```

### Adjust Number of Airports

Find this section (around line 360):
```javascript
for (let i = 0; i < 15; i++) {
    gameState.airports.push(generateAirport(i));
}
```

Change `15` to a different number:
- `5` = Few airports (harder to find)
- `15` = Default
- `50` = Many airports

### Change Landing Requirements

Find this section (around line 680):
```javascript
if (horizontalDist < nearest.size && altDiff < 100 && gameState.plane.speed < 100) {
```

Adjust these values:
- `nearest.size` = How close you need to be (200 is default)
- `100` = Maximum altitude difference
- `100` = Maximum speed for landing

Example (easier landing):
```javascript
if (horizontalDist < nearest.size * 1.5 && altDiff < 200 && gameState.plane.speed < 150) {
```

---

## Advanced Customization

### Change Terrain Generation

The terrain uses a noise function. Find (around line 220):
```javascript
for (let i = 0; i < 5; i++) {
    height += simpleNoise(x * frequency, z * frequency, seed + i) * amplitude;
    maxValue += amplitude;
    amplitude *= 0.5;
    frequency *= 2;
}
```

Adjust these for different terrain:
- More iterations = More detail (slower)
- `amplitude *= 0.7` = Smoother terrain
- `amplitude *= 0.3` = Rockier terrain
- `frequency *= 2` = Tighter features

### Add Different Weather

Add at the beginning of the animate loop:
```javascript
// Example: Wind effect
const windStrength = Math.sin(gameState.time * 0.01) * 0.5;
gameState.plane.velocity.x += windStrength;
```

### Custom Crosshair

Find the crosshair section (around line 140):
```css
.crosshair {
    width: 40px;
    height: 40px;
    border: 2px solid rgba(255, 100, 0, 0.6);
}
```

Make it larger or smaller:
- `40px` = Current size
- `60px` = Larger
- `20px` = Smaller

Change shape (add to `.crosshair`):
```css
border-radius: 0%;    /* Square */
border-radius: 50%;   /* Circle */
```

---

## Performance Optimization

### Reduce Terrain Quality (Better FPS)

Find this section (around line 270):
```javascript
const resolution = 32;
```

Lower the value:
- `16` = Lower quality, faster
- `32` = Default
- `64` = Higher quality, slower

### Disable Shadows (Better FPS)

Find this section (around line 170):
```javascript
renderer.shadowMap.enabled = true;
```

Change to:
```javascript
renderer.shadowMap.enabled = false;
```

### Reduce Terrain Chunk Distance

Find this section (around line 620):
```javascript
for (let dx = -3; dx <= 3; dx++) {
    for (let dz = -3; dz <= 3; dz++) {
```

Change `-3` to `-2` or `-1` for closer detail loading.

---

## Tips for Modding

1. **Always backup** your `index.html` before making changes
2. **Use browser console** (F12) to debug JavaScript errors
3. **Test locally** by opening the file in your browser
4. **Use comments** to remember what you changed
5. **Search for values** using Ctrl+F to find settings quickly
6. **Reload page** (Ctrl+R) to see changes

---

## Example Mod: Speed Run Mode

Want a challenging speed-run game? Try these settings:

```javascript
// Harder fuel consumption
gameState.plane.fuel -= 0.08;

// Fewer airports
for (let i = 0; i < 3; i++) {

// Less fuel to start
gameState.plane.fuel = 30;

// Strict landing requirements
if (horizontalDist < nearest.size * 0.8 && altDiff < 50 && gameState.plane.speed < 70) {
```

---

## Want Even More Control?

The entire game is in one HTML file with well-commented code. Feel free to:
- Modify the physics engine
- Add new features
- Change the HUD layout
- Add sound effects (using Web Audio API)
- Create multiplayer (using WebSockets)

Happy modding! 🛠️✈️
