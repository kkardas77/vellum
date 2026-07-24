with open('index.html', 'r') as f:
    html = f.read()

silktide = """
<!-- Silktide Consent Manager -->
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" id="silktide-consent-manager-css" href="https://cdn.jsdelivr.net/gh/silktide/consent-manager@v2.0.0/silktide-consent-manager.css" integrity="sha384-IO1E/jCrQXyH5rwcI0SXP7OXw47JFqQNDQcKhbFvqnL2IunBxxwE2Ne5XyAmCqKs" crossorigin="anonymous">
<style id="silktide-consent-manager-overrides">
#stcm-wrapper {
  --primaryColor: #C9A84C;
  --backgroundColor: #111009;
  --textColor: #f0ece4;
  --iconColor: #c9a84c;
  --iconBackgroundColor: #111009;
}
</style>
<script src="https://cdn.jsdelivr.net/gh/silktide/consent-manager@v2.0.0/silktide-consent-manager.js" integrity="sha384-j4NIMOecmtzMWe9GJADIIe5hTlHG63aiTQ/2XorW10RNyQJg+IU+xwFVDy45wBah" crossorigin="anonymous"></script>
<script>
window.silktideConsentManager.init({
  backdrop: { show: false },
  icon: { position: "bottomLeft" },
  prompt: { position: "bottomLeft" },
  consentTypes: [
    { id: "essential", label: "Essential", description: "<p>These cookies are necessary for the website to function properly.</p>", required: true },
    { id: "analytics", label: "Analytics", description: "<p>We use Google Analytics to understand how visitors interact with our website.</p>", defaultValue: true, gtag: "analytics_storage" },
    { id: "marketing", label: "Marketing", description: "<p>These cookies are used to show you relevant ads and measure campaign performance.</p>", gtag: ["ad_storage", "ad_user_data", "ad_personalization"] }
  ],
  text: {
    prompt: { description: "<p>We use cookies to enhance your experience and analyze our traffic.</p>", acceptAllButtonText: "Accept all", rejectNonEssentialButtonText: "Reject non-essential", preferencesButtonText: "Preferences" },
    preferences: { title: "Cookie preferences", description: "<p>You can choose not to allow some types of cookies.</p>", saveButtonText: "Save and close" }
  }
});
</script>
"""

html = html.replace('    <link rel="icon"', silktide + '    <link rel="icon"', 1)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
