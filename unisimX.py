import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# Hubble Sabiti (km/s/Mpc)
H0 = 70

# Uzaklık aralığı (Mpc)
d_min = 0.01
d_max = 10
num_points = 100

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Evrenin Genişleme Hızı")
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        
        # Grafik için figure oluşturuluyor
        fig_2d = plt.figure()
        
        canvas_2d = FigureCanvas(fig_2d)
    
        # Uzaklık değerlerini oluşturma 
        distances = np.linspace(d_min, d_max, num=num_points)

        # Genişleme hızını hesaplama (km/s) 
        velocities = H0 * distances

        # Grafik tablosunu çizme
        ax1 = fig_2d.add_subplot(111)
        ax1.plot(distances, velocities)
        ax1.set_xlabel('Uzaklık (Mpc)')
        ax1.set_ylabel('Genişleme Hızı (km/s)')
        
        layout.addWidget(canvas_2d)

        # 3D Şekli Oluşturma
        fig_3d = plt.figure()
        canvas_3d = FigureCanvas(fig_3d)
       
        distances_3d = np.linspace(d_min, d_max, num=num_points)
        velocities_3d = H0 * distances

        # Eksenlerin oluşturulması
        x_coords, y_coords, z_coords = [], [], []

        for i in range(len(distances)):
            x_coords.append(distances[i])
            y_coords.append(velocities[i])
            z_coords.append(0)  # Z ekseni sıfır
            
        ax2 = fig_3d.add_subplot(111, projection='3d')
        
        colors_normalized = [float(i) / len(x_coords) for i in range(len(x_coords))]
        
        scat_plot = ax2.scatter(xs=x_coords,
                                ys=y_coords,
                                zs=z_coords,
                                c=colors_normalized,
                                cmap=plt.cm.get_cmap("rainbow"),
                                alpha=0.7)

        cb_colorbar = plt.colorbar(scat_plot).set_label(label="Renk Değeri", size=10)

        ax2.set_xlabel('Uzaklık (Mpc)', fontsize=10)
        ax2.set_ylabel('Genişleme Hızı (km/s)', fontsize=10)
        ax2.view_init(elev=30, azim=-60)
        ax2.set_title('Evrenin Genişleme Hızı 3D', fontsize=12)

        layout.addWidget(canvas_3d)
        
        central_widget.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
