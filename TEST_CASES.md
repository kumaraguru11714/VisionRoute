# VisionRoute — Sample Test Cases

These are planned/manual test cases, not claims of completed validation. Record actual outcomes during testing.

| ID | Scenario | Expected behaviour | Actual result | Status |
|---|---|---|---|---|
| TC-01 | Person clearly visible in camera | Person box appears if model detects it | Fill after test | Not tested |
| TC-02 | Chair in front of camera | Chair label may appear if recognized | Fill after test | Not tested |
| TC-03 | No supported objects visible | No obstacle speech alert | Fill after test | Not tested |
| TC-04 | Object occupies a large part of frame | Spoken “possibly close” warning may be triggered | Fill after test | Not tested |
| TC-05 | Webcam disconnected or unavailable | Program reports camera error | Fill after test | Not tested |
| TC-06 | Low lighting / partial occlusion | Detection may be reduced; document failures | Fill after test | Not tested |
| TC-07 | Bluetooth headset paired and selected as system output | Speech should route to selected output if OS supports it | Fill after test | Not tested |
| TC-08 | Press `q` in preview window | Program exits and releases camera | Fill after test | Not tested |

## Test protocol
1. Run tests in a clear, controlled indoor space with a sighted helper.
2. Never use the prototype while crossing roads, near stairs, or in a moving environment.
3. Record model label, confidence, whether an alert occurred, and any false/missed detections.
4. Do not describe planned or unrun tests as passed.
