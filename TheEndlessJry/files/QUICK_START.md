# Quick Start Guide

## Get Started in 2 Minutes

### 1. Download Your Game

You have everything you need:
- `index.html` - The complete game (1 file, self-contained!)
- `README.md` - Full documentation
- `GITHUB_PAGES_SETUP.md` - Deployment guide
- `CUSTOMIZATION_GUIDE.md` - Modding instructions

### 2. Test Locally

**Desktop:**
1. Right-click `index.html`
2. Select "Open with" → Your web browser
3. Game loads instantly!

**Don't want to download?**
- You can also just copy the contents and paste into a `.html` file yourself

### 3. Deploy to GitHub Pages (30 seconds)

1. Go to [github.com](https://github.com)
2. Create new repository named: `your-username.github.io`
3. Click **Add file** → **Upload files**
4. Drag `index.html` onto the upload area
5. Click **Commit changes**
6. Wait 1-2 minutes
7. Visit: `https://your-username.github.io`

**Done! Your game is live!** 🎉

---

## Game Controls

| Action | Control |
|--------|---------|
| **Pitch (up/down)** | Move mouse up/down |
| **Roll (left/right)** | Move mouse left/right |
| **Speed up** | Scroll mouse wheel up |
| **Slow down** | Scroll mouse wheel down |
| **Land** | Press SPACE (when indicator shows) |
| **Reset** | Press R |

---

## How to Play

1. **Fly around** and explore the infinite world
2. **Watch your fuel** - it decreases constantly
3. **Find airports** - look for orange lights on the ground or green squares on radar
4. **Approach carefully:**
   - Slow down to < 100 knots
   - Descend gradually
   - Align with runway
5. **Land successfully** when indicator appears
6. **Fuel refills** - start again with 100% fuel

---

## HUD Explained

### Left Side Panels:

**ALTITUDE**
- Your height above sea level in feet
- Vertical speed in feet per second
- Climb higher = consume more fuel

**AIRSPEED**
- Your speed in knots
- Fuel percentage remaining
- Must slow down to land safely

**HEADING**
- Current direction (0-360°)
- Pitch angle (up/down tilt)
- For landing: align with runway

### Right Side:

**STATUS**
- Current flight status
- Nearest airport ID
- Distance to nearest airport in nautical miles

**RADAR** (bottom right)
- Center red dot = Your plane
- Green squares = Nearby airports
- Blue squares = Distant airports
- Rings = Distance markers

---

## Tips for Success

**Flying**
- ✈️ Gentle, smooth mouse movements = stable flight
- ✈️ Start at 500 feet altitude - plenty of time to explore
- ✈️ Faster speeds = more fuel consumption
- ✈️ Glide down gradually - don't dive!

**Landing**
- 🛬 Approach from straight ahead
- 🛬 Speed must be below 100 knots
- 🛬 Altitude should be low (close to runway)
- 🛬 Wait for orange indicator, then press SPACE
- 🛬 You'll get a success message!

**Fuel Management**
- ⛽ Watch your fuel percentage closely
- ⛽ Land when it gets low (below 30%)
- ⛽ Choose closer airports if fuel is critical
- ⛽ Ascending uses more fuel than level flight

---

## World Map

The world is **infinite** and **randomly generated**, but airports follow a pattern:

```
        AIRPORT 0
           |
    AIRPORT 14  AIRPORT 1
        \  |  /
         \ | /
    ------PLAYER------
         / | \
        /  |  \
    AIRPORT 13  AIRPORT 2
           |
        AIRPORT 12
```

- First few airports are closest (AIRPORT 0-2)
- Airports are arranged in a spiral around you
- Each airport is unique and at different altitudes
- Terrain between airports varies greatly

**Radar Pro Tip:** Use the radar to navigate! Watch for green squares approaching as you fly.

---

## Troubleshooting

**Game is slow?**
- Try a different browser (Chrome is fastest)
- Close other applications
- Reduce brightness (helps GPU focus on game)

**Can't control the plane?**
- Click inside the game window first
- Make sure mouse is over the canvas
- Try moving your mouse slowly

**Lost in the world?**
- Press R to reset to starting position
- Check radar for nearby airports
- Or just explore! No wrong direction.

**Crashing too much?**
- Fly higher (500+ feet)
- Check your altitude gauge
- Move mouse more carefully
- Watch out for terrain below!

**Game not loading?**
- Refresh page (Ctrl+R or Cmd+R)
- Try different browser
- Check you have WebGL (chrome://gpu)

---

## Next Steps

### Want to customize?
Read `CUSTOMIZATION_GUIDE.md` to:
- Change colors and visuals
- Adjust difficulty
- Modify controls
- Add new features

### Want to deploy?
Follow `GITHUB_PAGES_SETUP.md` for:
- Step-by-step GitHub Pages setup
- Custom domain options
- Keeping your game updated

### Want to show friends?
- Share your GitHub Pages link
- No installation needed
- Works on any device with a browser

---

## The Bottom Line

You have a **complete, professional flight simulator game** ready to:
- ✅ Play locally
- ✅ Customize
- ✅ Deploy online
- ✅ Share with the world

Everything is in `index.html`. It's about 500 lines of code with:
- 3D graphics (Three.js)
- Procedural terrain generation
- Physics simulation
- Professional HUD
- Landing mechanics
- Infinite world

**Just open it and fly!** ✈️

---

**Questions?** Check the full README.md for detailed information.

Happy flying! 🎮
