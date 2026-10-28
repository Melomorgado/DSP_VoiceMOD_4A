# DSP VoiceMOD 4A

A desktop application for voice cloning and digital audio processing.

## Installation and Setup

### 1. Clone the repository

Make sure Git and Python are installed, then run:

```bash
git clone https://github.com/Melomorgado/DSP_VoiceMOD_4A.git
```

### 2. Enter the project directory

```bash
cd DSP_VoiceMOD_4A
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Choose the command for your operating system.

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows — Command Prompt**

```bat
.venv\Scripts\activate.bat
```

**Windows — PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

After activation, your terminal prompt should indicate that `.venv` is active.

### 5. Install dependencies

With the virtual environment activated, run:

```bash
pip install -r reqs.txt
```

### 6. Launch the application

```bash
python ui.py
```

## First Launch and Initialization

**Please be patient when launching the application for the first time.** It may take a while to download and prepare the required Python dependencies and voice-model files. The duration depends on your internet connection and computer.

After the window opens, the application may display **Initializing...** while it prepares the voice-cloning model. Wait until initialization finishes and the status indicates that the model is ready before using voice cloning. Do not close the application while initialization is in progress.

On subsequent runs, the application still needs to initialize/load the model before voice cloning is ready. Previously downloaded files are normally reused, so the first launch generally takes longer than later launches.

## Running the Application Again

Whenever you want to start the application again:

1. Open a terminal in the `DSP_VoiceMOD_4A` directory.
2. Activate the virtual environment using the command for your operating system above.
3. Run:

   ```bash
   python ui.py
   ```

## Troubleshooting

- **`python` is not found:** Install Python and ensure it is available on your `PATH`. On some systems, you may need to use `python3` instead of `python` when creating the environment.
- **Dependency installation fails:** Verify your internet connection and check that the virtual environment is activated before running `python -m pip install -r reqs.txt` again.
- **Initialization takes a while:** Model files may need to download or load. Check the terminal for error messages and allow initialization to complete.
- **PowerShell blocks activation:** You can use Command Prompt activation instead, or follow your organization's guidance for PowerShell execution policies.

## Repository

https://github.com/Melomorgado/DSP_VoiceMOD_4A
