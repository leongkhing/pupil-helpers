# pupil-helpers

The pupil-helpers repository contains utility scripts and concise code examples that demonstrate how to communicate and develop your own tools with [Pupil](https://github.com/pupil-labs/pupil).

If you're new to Pupil, we highly recommend checking out the [docs](https://docs.pupil-labs.com).

For documentation on Pupil's message based API, please read through the [Networking](https://docs.pupil-labs.com/#networking) section in the docs.

For more information about plugin development, check out the [Plugin Guide](https://docs.pupil-labs.com/#plugin-guide).


#### Folder Content

- `python`: Example Python scripts that showcase interaction with Pupil Remote and the Pupil IPC
- `matlab`: Example Matlab scripts, see the folder's `README.md` for details
- `network_time_sync`: Spec and implementation for the Pupil Timesync Protocol
- `markers_stickersheet`: Surface marker images and vector files
- `write_your_own_plugin`: Example Pupil plugin

## Contributing

Pull Requests to this repo should be revisions of existing code. New examples should be referenced in the [pupil-community](https://github.com/pupil-labs/pupil-community) repository.




# For Eye Gaze interface
1. Install [Pupil](https://github.com/pupil-labs/pupil)
2. Run `Pupil`
3. Place ArUCo markers at the corners of the screen of the target computer.
4. Define a surface with the name "screen" using the `Surface Tracker` from `Pupil`.
5. `python python/blinkPub.py` : register a click when user close his eyes for 2 to 3 seconds.
6. `python python/mouse_control.py` : move the mouse cursor to user gaze point, when the user gaze fixed at a position on the screen for 10 seconds.

### note: 
- Ensure that the ip for both `blinkPub.py` and `mouse_control.py` are set to the computer that is running `Pupil`.
- Ensure that the `Network API`, `Surface Tracker` and `Blink Detector` are enabled when running `Pupil`.
