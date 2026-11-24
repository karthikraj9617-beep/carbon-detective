# Carbon Detective — Sustain World
A five-question exhibition game with participant registration, central storage and a password-protected Excel register.

## Upload to GitHub
Extract the ZIP. Create a repository in GitHub, select **uploading an existing file** (or **Add file → Upload files**), then upload the extracted files and folders. Keep public/, worker/, build.py and wrangler.toml at the repository root. Commit the changes.

## Publish the playable game
GitHub hosts the source. The full game uses Cloudflare Workers and D1 for registration and Excel export. GitHub Pages alone cannot run that backend. This deployment creates a new game URL and a separate participant database.

Install Python 3 (available as python), Node.js 22 or newer, and open a terminal at the repository root. Sign in to your Cloudflare account and create the database:
```sh
npx wrangler@4 login
npx wrangler@4 d1 create carbon-detective-participants
```
Copy the returned database ID into the existing database_id field in wrangler.toml and save. Retain DB as the binding name. Deploy:
```sh
npx wrangler@4 deploy
npx wrangler@4 secret put STAFF_PASSWORD
```
At the prompt, enter a strong new password. Share the deployed workers.dev URL with participants. The app creates the register table on first use. Open /staff/register.xlsx on that same domain to download the latest workbook with username **staff** and your new password.

## Booth check
Complete a test check-in and confirm its row in a fresh Excel download before opening the booth. Test entries are stored alongside real registrations. Existing hosted registrations remain in the original deployment.

## Project files
public/ contains the game, branding and questions. worker/ contains registration, Excel template data and staff export logic. build.py assembles the deployable Worker from these sources. Keep downloaded registers and credentials outside the repository.
