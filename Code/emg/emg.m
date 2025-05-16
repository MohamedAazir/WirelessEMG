% Parameters
ESP32_IP = 'http://192.168.4.1/'; % ESP32 IP Address
csvFileName = 'sine_wave_data.csv'; % File to save the data
samplingRate = 2000; % Sampling rate in Hz
f0 = 50; % Frequency to remove (50 Hz)
Q = 5; % Quality factor for notch filter

% Fetch data from ESP32
try
    sineWaveData = webread(ESP32_IP); % Fetch sine wave data
catch ME
    fprintf('Error fetching data from ESP32: %s\n', ME.message);
    return;
end

% Ensure data is numeric
sineWaveData = cell2mat(sineWaveData);

% Generate time axis
sampleCount = length(sineWaveData);
time = linspace(0, sampleCount / samplingRate, sampleCount);

% Save to CSV
try
    dataTable = table(time(:), sineWaveData(:), 'VariableNames', {'Time', 'Amplitude'});
    writetable(dataTable, csvFileName);
    fprintf('Sine wave data saved to %s\n', csvFileName);
catch ME
    fprintf('Error saving to CSV file: %s\n', ME.message);
    return;
end

% Design the notch filter
wo = f0 / (samplingRate / 2); % Normalized frequency
[b, a] = iirnotch(wo, wo / Q);

% Apply the notch filter
filteredSineWave = filtfilt(b, a, sineWaveData);

% Plot the original and filtered sine wave
figure;
subplot(2, 1, 1);
plot(time(1:500), sineWaveData(1:500), 'r');
title('Original Sine Wave');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

subplot(2, 1, 2);
plot(time(1:500), filteredSineWave(1:500), 'b');
title('Filtered Sine Wave (50 Hz Removed)');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;
