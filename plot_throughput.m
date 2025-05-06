% Gráfico de barras (Figure 1: Throughput)
figure;
bar(throughput);
set(gca, 'XTickLabel', methods, 'FontName', 'Palatino Linotype', 'FontSize', 18);  % Tamaño de número en ejes);
ylabel('Throughput (tasks/min)', 'FontName', 'Palatino Linotype', 'FontSize', 20);
title('Throughput Comparison Across Methods', 'FontName', 'Palatino Linotype', 'FontSize', 22);
% Simular métricas de rendimiento (valores del paper)
methods = {'Hybrid DL-RL', 'Rule-Based', 'SARSA'};
throughput = [12.5, 10.0, 10.8];
workload = [65.2, 76.8, 70.5];
safety = [98.5, 95.0, 96.5]; 

