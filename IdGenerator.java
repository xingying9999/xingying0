package com.test;

public class IdGenerator {

    private long timestamp;
    private long workerId;
    private long sequence;

    //距离2019-02-23T07:15:35.971Z 往后100年的时间戳占用43位
    private long timestampBits = 43;
    private long workerIdBits = 5;
    private long sequenceBits = 15;

    private long workerIdShift = sequenceBits;
    private long timestampShift = sequenceBits + workerIdBits;

    private long maxWorkerId = ~(-1L << workerIdBits);
    private long sequenceMask = ~(-1L << sequenceBits);

    public IdGenerator(long workerId) {
        if (workerId > maxWorkerId) {
            throw new RuntimeException("worker id over");
        }
        this.workerId = workerId;
        this.sequence = 0L;
        this.timestamp = timeGen();
    }

    public synchronized Long genId() {
        long lasttimestamp = timestamp;
        timestamp = timeGen();
        if (timestamp < lasttimestamp) {
            throw new RuntimeException("gen id error");
        }
        if (timestamp > lasttimestamp) {
            sequence = 0;
        } else {
            sequence = (sequence + 1) & sequenceMask;
            if (sequence == 0L) {
                timestamp = tilNextMillis(lasttimestamp);
            }
        }
        return timestamp << timestampShift | workerId << workerIdShift | sequence;
    }

    private long tilNextMillis(long lastTimestamp) {
        long timestamp = timeGen();
        while (timestamp <= lastTimestamp) {
            timestamp = timeGen();
        }
        return timestamp;
    }
    private long timeGen(){
        return System.currentTimeMillis();
    }

}
