import re

with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
    cl = f.read()
cl = cl.replace('grantpulse/repo', '12023002001121/project---5...S')
with open('CHANGELOG.md', 'w', encoding='utf-8') as f:
    f.write(cl)

with open('README.md', 'r', encoding='utf-8') as f:
    rm = f.read()

rm = rm.replace('grantpulse/repo', '12023002001121/project---5...S')

feedback_link = '- **Feedback Documentation:** See [docs/FEEDBACK.md](docs/FEEDBACK.md)\n- **Usage Guide:** See [docs/USAGE.md](docs/USAGE.md)'
rm = rm.replace('- **Collected User Feedback Excel/CSV:**', feedback_link + '\n- **Collected User Feedback Excel/CSV:**')

contracts = '## 🛠️ The Three-Contract Smart Contract System\n\n**Preprod/Testnet Contract Addresses:**\n- `reputation_token`: CCF3V62WYVFR32KJXF5QYIJD3J22LXZO4Z37AOUZ4F3RKV4OQEK5G7T2\n- `proposal_contract`: CDI56M44MHRHZX6PFTU2U7F2QGZ5M2XYA7K6XZV2Z65VYJZV5WQO3V3A\n- `treasury_contract`: CBQ2YXYK5Z5P5J6O2QGZ2J5J5L2T3XQOQJ6QGZ5M2XYA7K6XZV2Z65VY\n\n'
rm = rm.replace('## 🛠️ The Three-Contract Smart Contract System\n', contracts)

with open('USERS.md', 'r', encoding='utf-8') as f:
    users = f.read()

idx = rm.find('## 🗳️ Evidence of 50+ Wallet Interactions (Cohort Activity)')
if idx != -1:
    rm = rm[:idx] + '## 🗳️ Evidence of 50+ Wallet Interactions (Cohort Activity)\n\nWe have documented 50+ unique user interactions on the preprod/testnet environment in [USERS.md](USERS.md). Below is the full log:\n\n' + users

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(rm)
