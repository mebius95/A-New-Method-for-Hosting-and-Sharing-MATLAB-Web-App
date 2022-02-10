function out=ditong(ap,as,wp,ws)
    T=0.001;
    omegap=wp/T;
    omegas=ws/T;
    [N,wn]=buttord(omegap,omegas,ap,as,"s");
    [b,a]=butter(N,wn,"s");
    [bz,az]=impinvar(b,a,1/T);
    disp("分子系数b");
    fprintf("%.4e   ",bz);
    fprintf('\n');
    disp('分母系数a');fprintf('%.4e    ',az);fprintf('\n');
    omega=0:0.01:pi;
    h=freqz(bz,az,omega);
    out=N;
    ampli=20*log10(abs(h)/abs(h(1)));
    figure;
    plot(omega/pi,ampli,"k")
    xlabel("数字频率/\pi")
    ylabel("幅度/dB");grid;
    saveas(1,"D:\image\lowpassAM.jpg")
    theta=phasez(bz,az,omega);
    figure;
    plot(omega/pi,theta*360/(2*pi),"k")
    xlabel('数字频率/\pi');ylabel('相位/°');grid;
    saveas(2,"D:\image\lowpassPM.jpg")
end