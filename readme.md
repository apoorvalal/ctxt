## `ctxt` :  context builders

Command line programs in python and bash to recursively search for a user-provided filename pattern and dump contents into (an output file  | clipboard). Intended use is to build inputs for a context window for LLMs. Make them executable (`chmod +x ctxt.py` and/or `chmod +x ctxt.sh`) and put them somewhere your CLI can find them (i.e. in your `$PATH`, e.g. `~/.local/bin`).

Then, you can run
```
ctxt.py "_util*.py"
```

to copy the contents of all files matching `_util*.py` to your clipboard. If you're using wayland on linux, change xclip to wlclip. 

If you provide an additional argument `"output.txt"`, the contents of all matching files will be written to `output.txt`.

The output contains filenames with lines beginning `#!#`.

Inspired by [fasthtml's docs suggestion to upload a plaintext documentation file to Claude's context window](https://github.com/AnswerDotAI/fasthtml?tab=readme-ov-file#getting-help-from-ai)
