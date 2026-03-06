# Infinite Skies - Web-Based Plane Simulator

A complete browser-based endless plane simulator game with procedurally generated terrain, realistic flight mechanics, and interactive airports to discover and land on.

## Features

✈️ **Realistic Flight Physics**
- Mouse-based pitch and roll control
- Throttle control via scroll wheel
- Gravity and aerodynamics simulation
- Fuel management system

🌍 **Infinite Procedurally Generated World**
- Endless terrain generation using Perlin-like noise
- Dynamic chunk loading system
- 15+ randomly placed airports scattered across the map
- Realistic landing zones with visual runways

🎯 **Landing Mechanics**
- Proximity detection for landing zones
- Speed restrictions for safe landing
- Landing indicator with visual feedback
- Successful landing animations

📊 **Professional HUD**
- Real-time altitude, airspeed, and fuel display
- Heading and pitch instruments
- Radar with airport detection
- Distance to nearest airport
- Vertical speed indicator

🎮 **Intuitive Controls**
- **Mouse Movement**: Control pitch (up/down) and roll (left/right)
- **Mouse Scroll**: Adjust throttle/speed
- **SPACE**: Land at airport (when in landing zone)
- **R**: Reset flight

## How to Deploy to GitHub Pages

### Option 1: Quick Deployment (Recommended)

1. **Create a new GitHub repository** named `your-username.github.io`
   - Replace `your-username` with your actual GitHub username
   - This will be your main GitHub Pages site

2. **Add the files:**
   - Copy `index.html` to the root of your repository
   - Commit and push to `main` branch

3. **Access your game:**
   - Visit `https://your-username.github.io` in your browser
   - Your game is now live!

### Option 2: Using an Existing Repository

1. **Create a folder** (e.g., `plane-simulator`) in your repository

2. **Add the file:**
   - Place `index.html` in that folder

3. **Enable GitHub Pages:**
   - Go to repository **Settings** > **Pages**
   - Select source as `main` branch
   - Choose the `/docs` folder or `/root` if using root

4. **Access your game:**
   - Visit `https://your-username.github.io/plane-simulator/`

## Game Guide

### Objective
Fly your plane across an infinite randomly-generated world, discover airports, and practice your landing skills!

### Gameplay Tips

**Getting Started:**
1. Your plane spawns at 500 feet altitude with 100% fuel
2. Use your mouse to control pitch (vertical movement) and roll (banking)
3. Scroll to increase or decrease speed
4. Watch the altitude and fuel gauges

**Flying:**
- Move your mouse toward the top of the screen to pitch up (climb)
- Move your mouse toward the bottom to pitch down (descend)
- Move left/right to bank your plane
- Maintain moderate speed (80-120 knots) for efficient flying
- Avoid flying too low - you'll crash into terrain!

**Landing:**
- Check the "NEAREST AIRPORT" indicator in the HUD
- Watch your radar to spot nearby airports (green squares)
- Approach an airport with:
  - **Speed < 100 knots** (scroll to slow down)
  - **Low altitude** (glide down gradually)
  - **Aligned with runway** (gentle approach)
- When the orange "LANDING ZONE DETECTED" message appears, press **SPACE** to land
- Successful landing refills your fuel to 100%!

**Fuel Management:**
- Fuel decreases continuously as you fly
- Higher altitudes consume more fuel
- Run out of fuel and you'll lose altitude - land quickly!
- Each successful landing restarts your fuel at 100%

**Radar:**
- Center circle (red) = Your plane
- Green squares = Nearby airports
- Blue squares = Distant airports
- Concentric rings = Distance markers

### Customization

Want to customize your game? Edit `index.html`:

**Change map generation:**
- Modify `gameState.terrain.scale` (2000 is default)
- Adjust `terrainHeight()` function for different terrain types

**Adjust difficulty:**
- Change `gameState.plane.fuel` initial value (100 is default)
- Modify fuel consumption rate (currently 0.02 per frame)
- Adjust gravity (currently -0.5 per frame)

**Customize controls:**
- Modify `maxPitch` and `maxRoll` values in the animate loop
- Change speed increment in the scroll handler

**Plane appearance:**
- Edit the plane geometry (fuselage, wings, tail) in the Three.js section
- Change materials and colors

## Technical Details

### Technology Stack
- **Three.js**: 3D graphics rendering
- **WebGL**: Hardware-accelerated 3D graphics
- **Vanilla JavaScript**: Game logic and physics
- **HTML5 Canvas**: HUD and radar rendering

### Performance
- Target: 60 FPS on modern browsers
- Optimized terrain chunking system
- Efficient shadow mapping
- Dynamic geometry loading

### Browser Compatibility
- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Any modern browser with WebGL support

### Recommended Hardware
- Desktop or laptop with dedicated GPU
- Minimum 4GB RAM
- Modern processor

## Troubleshooting

**Game not loading?**
- Check browser console (F12) for errors
- Ensure WebGL is enabled in your browser
- Try a different browser

**Low FPS/Lag?**
- Reduce terrain resolution (change `resolution: 32` to lower value)
- Disable shadows (set `renderer.shadowMap.enabled = false`)
- Close other applications

**Controls not responding?**
- Ensure your mouse is over the canvas
- Check that scroll wheel is not disabled
- Try pressing R to reset

## Future Enhancements

Potential features to add:
- [ ] Multiple aircraft with different characteristics
- [ ] Weather system (wind, storms)
- [ ] Day/night cycle
- [ ] Traffic and other aircraft
- [ ] Cockpit interior view
- [ ] Sound effects and engine audio
- [ ] Multiplayer support
- [ ] Touch controls for mobile
- [ ] Scoring/leaderboard system
- [ ] Hangar for aircraft customization

## Credits

Built with:
- Three.js by mrdoob and contributors
- WebGL specifications
- Modern web standards

## License

Free to use, modify, and distribute. Have fun flying!

---

**Happy Flying!** ✈️

For updates and improvements, visit the repository on GitHub.
