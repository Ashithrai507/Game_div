# 🎮 Game Visual Guide & HUD Layout

## Game Screen Layout

```
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  ┌──────────────┐                                                           ║
║  │   ALTITUDE   │                                                           ║
║  │   1,500 ft   │                                                  ┌─────────┤
║  │              │                                                  │ STATUS  │
║  │  VERT SPEED  │                                                  │ Flying  │
║  │   5.2 ft/s   │                                                  │         │
║  └──────────────┘                        [GAME VIEWPORT]           │ Airport │
║                                          (3D Plane View)           │ #7     │
║  ┌──────────────┐                                                  │         │
║  │  AIRSPEED    │                                                  │ Distance│
║  │   95 knots   │                                                  │ 3.2 nm  │
║  │              │                                                  └─────────┘
║  │  FUEL        │                                                  
║  │  75%         │                              ⊗ Crosshair
║  └──────────────┘                                                  
║                                                                     ┌─────────┐
║  ┌──────────────┐                                                  │ RADAR   │
║  │  HEADING     │                                                  │ █ ░ ░   │
║  │  245°        │                                                  │ ░ █ ░   │
║  │              │                                                  │ ░ ░ ░   │
║  │  PITCH       │                                                  │ (Radar  │
║  │  -2.5°       │                                                  │  View)  │
║  └──────────────┘                                                  └─────────┘
║                                                                              ║
║  ┌──────────────┐                                                           ║
║  │ CONTROLS     │                                                           ║
║  │ Mouse: Pitch │                                                           ║
║  │ Scroll: Spd  │                                                           ║
║  │ Space: Land  │                                                           ║
║  │ R: Reset     │                                                           ║
║  └──────────────┘                                                           ║
║                                                                              ║
║                      [LANDING INDICATOR - appears when ready]               ║
║                                                                              ║
╚════════════════════════════════════════════════════════════════════════════╝

█ = Player plane
░ = Airport on radar
```

---

## HUD Panel Breakdown

### LEFT SIDE PANELS

#### ALTITUDE Panel (Top Left)
```
┌─────────────────────┐
│   ALTITUDE          │
│   2,500 ft          │
│                     │
│   VERTICAL SPEED    │
│   -3.2 ft/s         │
└─────────────────────┘
```

**What it means:**
- **ALTITUDE**: Your height above ground in feet
  - 0-500 ft = Low altitude (landing zone)
  - 500-2000 ft = Cruise altitude
  - 2000-3000 ft = High altitude
- **VERTICAL SPEED**: How fast you're climbing (+) or descending (-)
  - Positive = climbing
  - Negative = descending
  - Close to 0 = level flight

#### AIRSPEED Panel
```
┌─────────────────────┐
│   AIRSPEED          │
│   120 knots         │
│                     │
│   FUEL              │
│   50%               │
└─────────────────────┘
```

**What it means:**
- **AIRSPEED**: Your forward speed in knots
  - 20-50 knots = Very slow (landing speed)
  - 50-100 knots = Normal cruise
  - 100-200 knots = Fast cruise
  - 200 knots = Maximum speed
- **FUEL**: Percentage of fuel remaining
  - 100% = Full tank
  - 50% = Half tank (plan landing)
  - 10% = Critical (land immediately!)
  - 0% = Stall out and crash

#### HEADING Panel
```
┌─────────────────────┐
│   HEADING           │
│   180°              │
│                     │
│   PITCH             │
│   5.3°              │
└─────────────────────┘
```

**What it means:**
- **HEADING**: Your compass direction
  - 0° = North (up)
  - 90° = East (right)
  - 180° = South (down)
  - 270° = West (left)
- **PITCH**: Your nose angle relative to horizon
  - Positive (+) = Nose up (climbing)
  - Negative (-) = Nose down (descending)
  - 0° = Level flight

---

### RIGHT SIDE PANELS

#### STATUS Panel (Top Right)
```
┌──────────────────────────┐
│   STATUS                 │
│   Flying                 │
│                          │
│   NEAREST AIRPORT: #3    │
│   DISTANCE: 5.2 nm       │
└──────────────────────────┘
```

**What it means:**
- **STATUS**: Your current state
  - "Flying" = Normal flight
  - "Landing Zone Detected" = Ready to land
- **NEAREST AIRPORT**: ID of closest airport
  - Airports numbered 0-14
  - Find the ones with landing lights
- **DISTANCE**: Nautical miles to nearest airport
  - 1 nm = 1.15 miles = 1.85 km
  - <1 nm = Very close
  - 10+ nm = Distant

#### RADAR Panel (Bottom Right)
```
┌──────────────────────────┐
│   RADAR                  │
│     ░   ░                │
│   ░       ░              │
│ ░    █     ░             │
│   ░       ░              │
│     ░   ░                │
└──────────────────────────┘
```

**Understanding the Radar:**
- **█ (Red center dot)** = Your airplane
- **░ (Green square)** = Nearby airport
- **░ (Blue square)** = Distant airport
- **Concentric circles** = Distance markers
  - Each ring = ~500m distance
  - Compass lines = Cardinal directions

**How to use it:**
1. Look for green squares (close airports)
2. Green squares move toward center = heading toward airport
3. Green squares move away = flying away from airport
4. Use radar to navigate toward airports for landing

---

## HUD Colors & Meanings

| Color | Location | Meaning |
|-------|----------|---------|
| **Green (#00ff41)** | Entire HUD | Normal/good status |
| **Orange (#ff6600)** | Landing indicator | Landing zone detected |
| **Red** | Plane on radar | Your position |
| **Green** | Radar | Nearby airports |
| **Blue** | Radar | Distant airports |

---

## Flight States

### NORMAL FLIGHT
```
Status: Flying
Altitude: 500+ ft
Speed: 80-150 knots
Fuel: 30%+ remaining

↓ What to do:
- Explore the world
- Look for airports
- Adjust altitude as needed
```

### APPROACHING AIRPORT
```
Status: Flying
Distance: < 5 nm
Look at Radar: Green square approaching center

↓ What to do:
- Slow down
- Start descending
- Align with runway
```

### LANDING ZONE DETECTED
```
Status: LANDING ZONE DETECTED (orange indicator)
Altitude: < 100 ft
Speed: < 100 knots
Horizontal distance: < 500 m

↓ What to do:
- Press SPACE to land
- You'll see success message
- Fuel refills to 100%
```

### LOW FUEL WARNING
```
Status: Flying
Fuel: < 10%

↓ What to do:
- Find nearest airport immediately
- Ignore all other considerations
- Head toward green radar square
- LAND ASAP!
```

---

## Control Sensitivity Guide

### MOUSE PITCH CONTROL
```
Mouse at TOP of screen
    ↑
    │
    ├─── PITCH UP (climb)
    │
At CENTER ─── LEVEL FLIGHT
    │
    ├─── PITCH DOWN (descend)
    │
    ↓
Mouse at BOTTOM of screen
```

### MOUSE ROLL CONTROL
```
LEFT ─── ROLL LEFT ──┐
                     ├─── CENTER ─── LEVEL WINGS ─── CENTER
RIGHT ─── ROLL RIGHT┘
```

**Responsiveness Tips:**
- **Small movements** = Smooth, precise control
- **Large movements** = Abrupt, dramatic changes
- **Centered mouse** = Neutral, stable flight
- **Hold position** = Maintains current attitude

---

## Crosshair Guide

The crosshair in the center shows your heading:

```
        ┌─────┐
        │     │
    ━━━━━  ⊗  ━━━━━
        │     │
        └─────┘
```

- **Center dot** = Your exact heading
- **Box around it** = Gimbals/reference
- **Stays centered** = Level flight
- **Moves up** = Pitching up
- **Moves side** = Rolling

---

## Reading Flight Data

### What "knots" means:
- 1 knot = 1 nautical mile per hour
- 1 knot ≈ 1.15 mph ≈ 1.85 km/h
- 100 knots ≈ 115 mph ≈ 185 km/h
- **Common speeds:**
  - 50 knots = Slow flight
  - 100 knots = Normal cruise
  - 150 knots = Fast cruise
  - 200 knots = Maximum speed

### What "nautical miles" means:
- 1 nm = 1.15 standard miles
- 1 nm ≈ 1.85 kilometers
- **Common distances:**
  - 0-1 nm = Very close (landing)
  - 1-5 nm = Close
  - 5-10 nm = Moderate distance
  - 10+ nm = Far away

### What degrees of pitch/heading mean:
- **Heading (0-360°):**
  - 0° = North
  - 90° = East
  - 180° = South
  - 270° = West
  
- **Pitch (-90 to +90°):**
  - -90° = Pointing straight down
  - -45° = Steep dive
  - 0° = Level
  - +45° = Steep climb
  - +90° = Pointing straight up

---

## Landing Procedure (Visual)

### Step 1: APPROACH
```
↓ Watch Radar
  Green square approaches center
  
↓ Distance decreases
  "Distance: 8.2 nm" → "Distance: 1.5 nm"
```

### Step 2: DESCEND
```
↓ Reduce throttle (scroll down)
  Altitude decreases slowly
  
↓ Maintain control
  Don't dive too steeply
  Watch airspeed
```

### Step 3: ALIGN
```
↓ Match plane heading to runway
  (Use compass heading)
  
↓ Adjust for wind/drift
  Small mouse movements
```

### Step 4: FINAL APPROACH
```
↓ Altitude: < 200 ft
  Speed: < 100 knots
  Distance: < 1 nm
  
↓ Crosshair centered
  Smooth, gentle descent
```

### Step 5: LANDING
```
↓ Orange indicator appears
  "LANDING ZONE DETECTED"
  
↓ Press SPACE
  Plane touches down
  
↓ Success message appears
  Fuel refills to 100%
```

---

## Emergency Procedures

### OUT OF FUEL
```
Problem: Fuel at 0%

Symptoms:
- Plane loses altitude rapidly
- Can't climb anymore
- Descending at high rate

Emergency:
- Land immediately (< 1 min before crash)
- Head toward nearest airport
- Don't worry about speed/angle
- Just get down safely
```

### TERRAIN COLLISION
```
Problem: Flying too low

Symptoms:
- Altitude approaches ground terrain
- Terrain visible on screen
- Height indicator near 0 ft

Emergency:
- Pitch up immediately (move mouse up)
- Add power (scroll up for speed)
- Climb to 500+ ft
- Be smooth with controls
```

### STALL/LOSS OF CONTROL
```
Problem: Flying too slow or too high pitch

Symptoms:
- Plane doesn't respond well to controls
- Won't gain altitude
- Falls out of sky

Emergency:
- Lower nose (mouse down slightly)
- Increase speed (scroll up)
- Recover to level flight
- Gentle corrections only
```

---

## Tips for Better Flying

### Smooth Movements
- Use gentle mouse movements
- Avoid jerky inputs
- Small corrections > large corrections

### Speed Management
- Different speeds for different situations:
  - Takeoff/climb: 100+ knots
  - Cruise: 80-120 knots
  - Approach: 70-90 knots
  - Landing: 40-70 knots

### Altitude Management
- Climb gradually (2-5° pitch)
- Descend gradually (2-5° pitch)
- Never dive steeply unless recovering
- Maintain at least 100 ft altitude

### Fuel Planning
- Start with 100% fuel
- Monitor fuel gauge continuously
- Land when fuel < 30%
- Don't let fuel reach 0%

### Navigation
- Use radar to find airports
- Watch heading indicator
- Adjust course gradually
- Plan route in advance

---

## Keyboard Reference Card

```
╔════════════════════════════════════════════╗
║         KEYBOARD REFERENCE                 ║
╠════════════════════════════════════════════╣
║  PRIMARY CONTROLS:                         ║
║  • MOUSE MOVEMENT ........ Pitch & Roll    ║
║  • SCROLL WHEEL .......... Throttle        ║
║                                            ║
║  SECONDARY CONTROLS:                       ║
║  • SPACEBAR ............. Land (at airport)║
║  • R ..................... Reset Flight   ║
║                                            ║
║  TIPS:                                     ║
║  • Click canvas first if controls slow     ║
║  • Smooth mouse = stable flight            ║
║  • Center mouse = level flight             ║
║  • Scroll slow/steady = smooth speed change║
╚════════════════════════════════════════════╝
```

---

## Screen Resolution Notes

Game works at ANY resolution:
- **Small screens** (1024x768): Still playable
- **Standard** (1920x1080): Ideal
- **Large** (2560x1440): Ultra clear
- **Ultra-wide** (3440x1440): Immersive
- **Mobile** (1080x1920): Rotated view

HUD automatically scales to fit your screen!

---

This visual guide should help you understand and navigate the HUD. Refer back here whenever you need clarification on what a gauge means or how to interpret the instruments!

**Happy flying!** ✈️
