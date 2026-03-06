# GitHub Pages Deployment Guide

## Step-by-Step Setup

### Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click the **+** icon in top right → **New repository**
3. For a personal GitHub Pages site:
   - Repository name: `your-username.github.io`
   - Replace `your-username` with your actual GitHub username
   - Example: `john-doe.github.io`

4. For a project repository:
   - Use any name (e.g., `plane-simulator`)
   - Repository name, description, public/private
   - Click **Create repository**

5. Click **Create repository**

### Step 2: Upload Files

#### Method A: Using GitHub Web Interface (Easiest)

1. In your new repository, click **Add file** → **Upload files**
2. Drag and drop `index.html` and `README.md`
3. Scroll down and click **Commit changes**

#### Method B: Using Git Command Line

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-username.github.io.git
   cd your-username.github.io
   ```

2. Copy files into the folder:
   ```bash
   cp index.html .
   cp README.md .
   ```

3. Commit and push:
   ```bash
   git add .
   git commit -m "Add plane simulator game"
   git push origin main
   ```

### Step 3: Enable GitHub Pages

#### For `your-username.github.io` repository:
- GitHub Pages is automatic!
- Your site goes live at `https://your-username.github.io`
- May take 1-2 minutes to deploy

#### For other repositories:

1. Go to repository **Settings**
2. Scroll to **Pages** section
3. Under "Source", select:
   - Branch: `main`
   - Folder: `/root` or `/(root)`
4. Click **Save**
5. Your site will be at: `https://your-username.github.io/repo-name/`

### Step 4: Access Your Game

Wait 1-2 minutes after pushing, then visit:
- `https://your-username.github.io` (for `username.github.io` repo)
- `https://your-username.github.io/plane-simulator` (for other repos)

That's it! Your game is live! 🎉

---

## Custom Domain (Optional)

To use your own domain:

1. Go to repository **Settings** > **Pages**
2. Under "Custom domain", enter your domain
3. Add DNS records provided by GitHub to your domain registrar

See [GitHub's custom domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site) for details.

---

## Troubleshooting

### Site not loading?
- Wait 1-2 minutes after pushing (GitHub needs time to deploy)
- Check repository settings > Pages to ensure source is correct
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)

### Getting 404 error?
- Verify `index.html` is in the root of your repository
- Check the correct URL for your site type
- Repository must be public for GitHub Pages to work

### Can't see my changes?
- Hard refresh browser: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
- Check GitHub Actions tab to see deployment status

---

## Keeping Your Game Updated

### To update your game:

1. Make changes locally to `index.html`
2. Commit and push:
   ```bash
   git add index.html
   git commit -m "Update game features"
   git push origin main
   ```
3. Changes should appear within 1-2 minutes

---

## Project Structure

```
your-username.github.io/
├── index.html       (Your game file)
└── README.md        (Documentation)
```

That's all you need! The game is completely self-contained in a single HTML file.

---

## Going Live Checklist

- [ ] Created GitHub account
- [ ] Created new repository (named correctly)
- [ ] Uploaded `index.html` to root
- [ ] Uploaded `README.md` (optional but recommended)
- [ ] Enabled GitHub Pages (if needed)
- [ ] Waited 1-2 minutes for deployment
- [ ] Tested the game in browser
- [ ] Game loads and runs smoothly
- [ ] Shared link with friends!

---

Happy flying! 🎮✈️
