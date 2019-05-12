import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

public class Scheduler {
	private static ScheduledExecutorService executor;

	public static void main(String args[]) {
	    executor = Executors.newSingleThreadScheduledExecutor();

	    ScheduledFuture<?> future = solution( () -> System.out.println("The Job Scheduler has done the second job"), 3000);

	    ScheduledFuture<?> future2 = solution( () -> System.out.println("The Job Scheduler has done the first job"), 2000);

	    // Cleanup
	    executor.shutdown();
	    executor = null;
	}

	public static ScheduledFuture<?> solution(Runnable command, int delay_ms) {
	    return executor.schedule( command, delay_ms, TimeUnit.MILLISECONDS );
	}
}
