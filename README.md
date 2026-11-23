# CNS Python Lab Programs

Short Python lab programs for Experiments 1, 2, 3, 4, 6, 7, and 8.

| File | Experiment |
|---|---|
| `exp1.py` | Caesar Cipher |
| `exp2.py` | Transposition Cipher |
| `exp3.py` | Image Steganography |
| `exp4.py` | GCD and Modular Inverse |
| `exp6.py` | AES Encryption and Decryption |
| `exp7.py` | ECB and CBC Modes |
| `exp8.py` | RSA Encryption and Decryption (simple for-loop version) |

## PowerShell

```powershell
git clone https://github.com/Saitanveesh/c.git
cd c
py -m pip install -r requirements.txt
py exp1.py
```

For other experiments, run `py exp2.py`, `py exp3.py`, `py exp4.py`, `py exp6.py`, `py exp7.py`, or `py exp8.py`.

## Ubuntu

```bash
sudo apt update
sudo apt install -y git python3 python3-venv
git clone https://github.com/Saitanveesh/c.git
cd c
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python exp1.py
```

To get later updates, run `git pull` inside your existing `c` directory.

## Sample inputs

- Exp 1: `HELLO`, key `3`.
- Exp 2: `HELLOWORLD`, key `4`.
- Exp 3: `HELLO`; place `flower.png` beside the script or it automatically creates a blank sample PNG. Output is `stego.png`.
- Exp 4: `48`, `18`, then `3`, `11`.
- Exp 6: `CRYPTOGRAPHY`.
- Exp 7: `CRYPTOGRAPHY LAB`.
- Exp 8: `p=17`, `q=11`, `e=7`, message `HELLO`.

These are teaching implementations, not production cryptography. AES-ECB leaks repeated-block patterns; production encryption should use an authenticated mode such as AES-GCM. RSA here is a small-number classroom demonstration.