import turicreate as tc

# Load the data
data =  tc.SFrame('yolo_food.sframe')

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Create a model
model = tc.object_detector.create(train_data, max_iterations=500)

# Save predictions to an SArray
predictions = model.predict(test_data)

# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test_data)

# Save the model for later use in Turi Create
model.save('yolo_food.model')

# Export for use in Core ML
model.export_coreml('yolo_food.mlmodel')