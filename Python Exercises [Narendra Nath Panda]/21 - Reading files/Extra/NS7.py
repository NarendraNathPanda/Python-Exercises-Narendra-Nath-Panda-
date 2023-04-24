def read_label_from_txt(label_path):
    """Read label from txt file."""
    text = np.fromfile(label_path)
    bounding_box = []
    with open(label_path, "r") as f:
        labels = f.read().split("\n")
        for label in labels:
            label = label.split(" ")
            if label and label[0] == ("Car" or "Van"): #  or "Truck"
                bounding_box.append(label[8:15])

    if bounding_box:
        data = np.array(bounding_box, dtype=np.float32)
        return data[:, 3:6], data[:, :3], data[:, 6]
    else:
        return None, None, None 