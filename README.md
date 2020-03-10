# rpm spec file for rocksdb

This can be used with [substrate](https://github.com/paritytech/substrate), either linking
dynamically or statically.

The usage of rocksdb here is not limited to this.

## Usage

This RocksDB package avoids re-compilation during
the substrate build process.

## rust / librocksdb-sys

All information is derived from: 

https://github.com/rust-rocksdb/rust-rocksdb/blob/master/librocksdb-sys/build.rs

### dyn-so linkage

```zsh
export ROCKSDB_LIB_DIR=/usr/lib64
```

is sufficient, given `lz4`, `zlib`, `zippy`, `bzip2` are available in standard lookup directories.

By default `librocksdb-sys` compiles all compression libs depending on the features activated. To use the system ones export them:

```zsh
export ROCKSDB_LIB_DIR=/usr/lib64 # duplicated
export ZLIB_LIB_DIR=/usr/lib64
export ZSTD_LIB_DIR=/usr/lib64
export LZ4_LIB_DIR=/usr/lib64
export BZIP2_LIB_DIR=/usr/lib64
export BZ2_LIB_DIR=/usr/lib64
export SNAPPY_LIB_DIR=/usr/lib64
```

### static linkage

**CURRENTLY NOT WORKING AS EXPECTED**


```zsh
export ROCKSDB_STATIC=1
export ZLIB_STATIC=1
export ZSTD_STATIC=1
export LZ4_STATIC=1
export BZIP2_STATIC=1
export BZ2_STATIC=1
# export SNAPPY_STATIC=1
```

are necessary for linking them statically with rust.

It is also necessary to link them during the compilation of rocksdb, and currently it is not clear how to achieve this without breakage just yet.


# Credits

## Prior Art

https://github.com/ray2501/librocksdb-spec
https://github.com/myheritage/rocksdb-rpm